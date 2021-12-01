import { StatusBar } from 'expo-status-bar';
import React, { useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Button } from 'react-native';
import { useState} from 'react';
import { ActivityIndicator } from 'react-native';
import Amplify from 'aws-amplify';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createDrawerNavigator } from '@react-navigation/drawer';
import config from './src/aws-exports';
Amplify.configure({
  ...config,
  Analytics: {
    disabled: true,
  },
});
import SignIn from './src/screens/SignIn';
import SignUp from './src/screens/SignUp';
import ConfirmSignUp from './src/screens/ConfirmSignUp';
import Home from './src/screens/Home';
import Ingredient from './src/screens/Ingredient';
import Allergy from './src/screens/Allergy';
import CookingStart from './src/screens/CookingStart';


import { withAuthenticator } from 'aws-amplify-react-native';


const AuthenticationStack = createStackNavigator();
const AppStack = createStackNavigator();
const DrawerAppStack = createDrawerNavigator();
const AuthenticationNavigator = props => {
  return (
    <AuthenticationStack.Navigator headerMode="none">
      <AuthenticationStack.Screen name="SignIn">
        {screenProps => (
          <SignIn {...screenProps} updateAuthState={props.updateAuthState} />
        )}
      </AuthenticationStack.Screen>
      <AuthenticationStack.Screen name="SignUp" component={SignUp} />
      <AuthenticationStack.Screen
        name="ConfirmSignUp"
        component={ConfirmSignUp}
      />
    </AuthenticationStack.Navigator>
  );
};

// If only one home screen not a Drawer
const AppNavigator = props => {
  return (
    <AppStack.Navigator>
      <AppStack.Screen name="Home">
        {screenProps => (
          <Home {...screenProps} updateAuthState={props.updateAuthState} />
        )}
      </AppStack.Screen>
    </AppStack.Navigator>
  );
};

const DrawerAppNavigator = props => {
  return (
    <DrawerAppStack.Navigator>
      <DrawerAppStack.Screen name="Home">
        {screenProps => (
          <Home {...screenProps} updateAuthState={props.updateAuthState} />
        )}
      </DrawerAppStack.Screen>
      <DrawerAppStack.Screen name="Allergy" component={Allergy} />
      <DrawerAppStack.Screen name="Ingredient" component={Ingredient} />
      <DrawerAppStack.Screen name="CookingStart" component={CookingStart} />
    </DrawerAppStack.Navigator>
  );
};

const Initializing = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <ActivityIndicator size="large" color="tomato" />
    </View>
  );
};

function App() {
  const [isUserLoggedIn, setUserLoggedIn] = useState('initializing');
    
  async function signOut() {
    try {
      await Auth.signOut();
    } catch (error) {
      console.log('Error signing out: ', error);
    }
  }

  useEffect(() => {
            checkAuthState();
          }, []);
              async function checkAuthState() {
            try {
              await Auth.currentAuthenticatedUser();
              console.log(' User is signed in');
              setUserLoggedIn('loggedIn');
            } catch (err) {
              console.log(' User is not signed in');
              setUserLoggedIn('loggedOut');
            }
          }
              function updateAuthState(isUserLoggedIn) {
            setUserLoggedIn(isUserLoggedIn);
          }
        
          return (
                    <NavigationContainer>
                        {isUserLoggedIn === 'initializing' && <Initializing />}
                        {isUserLoggedIn === 'loggedIn' && (
                            <DrawerAppNavigator updateAuthState={updateAuthState} />
                        )}
                        {isUserLoggedIn === 'loggedOut' && (
                            <AuthenticationNavigator updateAuthState={updateAuthState} />
                        )}
                           </NavigationContainer>
                       );
                 }

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
export default App;