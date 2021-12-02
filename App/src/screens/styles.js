import { StyleSheet } from "react-native";

const styles = StyleSheet.create({

    image: {
        width: '100%',
        height: 400,
        resizeMode: 'contain',
        alignItems:'center',
        marginTop:20,
        
        
    

    },
    title:{
        fontSize:50,
        color:'black',
        height:300,
        fontFamily:'LobsterTwo-Italic',
        
        

    },

    button:{
        backgroundColor:'red',
        width:200,
        height:50,
        alignItems: 'center',
        justifyContent:'center',
        borderRadius:90,
        marginTop:50,


    },
    
    button_text:{
        fontSize:20,
        color:'black',
        
        


    },

    text_under_button:{
        fontSize:20,
        color:'gray',
        height:300,
        marginTop: 90,


    }

    


});

export default styles;