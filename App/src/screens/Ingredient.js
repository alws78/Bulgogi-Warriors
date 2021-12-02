import { placeholder } from "@babel/types";
import React, {useState} from "react";
import { View,Text, TextInput, Button, StyleSheet, FlatList,TouchableOpacity} from "react-native";
import styles from "./IngredientStyles";

const Ingredients = (props) =>{


    const [enteredGoal,setEnteredGoal]=useState('');
    const [courseGoals,setCourseGoals]=useState([]);

    const shouldDisplayClearButton = enteredGoal.length > 0
    const shouldDisplayAllergy = enteredGoal.length > 0
    
    const InputHandler = (enteredText) =>{
        setEnteredGoal(enteredText);
    };

    const addInput = () =>{
        setCourseGoals ([...courseGoals,{id:Math.random().toString(),value:enteredGoal}]);
    };

    deleteItemById = id => {
        const filteredData = courseGoals.filter(item => item.id !== id);
        setCourseGoals([...filteredData]); /*,{id:Math.random().toString(),value:enteredGoal}]);*/
        
      };
    
    return(
        <View style ={styles.container}>
            <Text style ={styles.allergy_title}>Ingredients</Text> 
            <TextInput 
                style ={styles.textInput} 
                placeholder= {"Enter the ingredients you have..."} 
                value={enteredGoal}
                onChangeText = {InputHandler}
            />
            <Button style={styles.button_add} color="orange" title="+" onPress={()=> {addInput(); setEnteredGoal('');}} />
            
            <Text>
            {shouldDisplayClearButton && 
            <TouchableOpacity style={styles.button_delete}>
                 <Button color="gray" title="Clear" onPress ={ () => setEnteredGoal('')} /> 
            </TouchableOpacity> 
                }
            </Text>
        
            <View >

                {<FlatList data ={courseGoals} extraData={courseGoals} keyExtractor={(item) =>item.id.toString()}  
                    renderItem={itemData => ( 
                    <View style={styles.before_button_x}>  
                        <Text style ={styles.text_allergy} onPress= {() => deleteItemById(itemData.item.id)} >{itemData.item.value}
                        
                        
                        {itemData.item.value.length !==0 && 
                            <Button 
                            title="x" color="gray" 
                            onPress={() => deleteItemById(itemData.item.id)}>
                            </Button>}
                        
                        </Text>
                    </View>)}
                />}

            </View>
        </View>        
    );
};


export default Ingredients;