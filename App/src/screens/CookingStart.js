import React from "react";
import {View,Text, ImageBackground,Image, Pressable} from 'react-native';
import styles from "./styles";

const HomeScreen = (props) =>{
    return(
        <View style={{justifyContent:'center', alignItems:'center', backgroundColor: 'orange'}}>
            <Text style ={{marginTop: 85}}></Text>
            
            <ImageBackground source={require('../../assets/images/new_cloche.png')} 
            style ={styles.image}>
                {/*title*/}
                {/*Button*/}

                <Text style= {styles.title}>Ghost cooking </Text>

                <Pressable 
                style={styles.button} 
                onPress ={()=> alert("Let's cook button has been pressed")}>
                        <Text style= {styles.button_text}>요리를 합시다</Text>

                </Pressable>

            </ImageBackground>

            
            <Text style= {styles.text_under_button}>맛있는 음식을 같이 만듭시다 </Text>

        </View>
    );
};

export default HomeScreen ;