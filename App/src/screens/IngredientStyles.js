import { StyleSheet } from "react-native";
import styles from "./styles";

const styles_ingredients = StyleSheet.create({

    container:{
        margin:10,
        
    },

    textInput:{
        fontSize:20,
        padding:10,
        marginTop: 20,
        marginBottom:30,
        fontFamily:'Pacifico-regular',
        borderColor: 'gray',
         borderWidth: 1, 
         color : "blue",
         borderRadius:30,
    },

    allergy_title:{
        fontSize:60,
        fontFamily:'LobsterTwo-Italic',
        margin:10,
        marginLeft:75,
        color:"orange",
    },

    button_add:{
        width:100,
        height:30,
        borderRadius:90,
        marginTop:20,
        


    },

    text_allergy:{
        fontSize:20,
        margin:10,
        marginLeft:10,
    },

    button_delete:{
        height: 40,
        width:160,
        borderRadius:10,
        backgroundColor : "gray",
        marginLeft :50,
        marginRight:50,
        marginTop :20
    },

    before_button_x:{
        height: 60,
        width:150,
        borderRadius:40,
        marginLeft :10,
        

    },

    button_x:{
        height: 70,
        width:10,
        borderRadius:30,
        marginLeft :70,
        marginTop :1,

    },

    


});

export default styles_ingredients;