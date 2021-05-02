package com.messaging.cdss;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText editText;
    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editText = findViewById(R.id.editText);
        button = findViewById(R.id.Submit);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (editText.getText().toString().isEmpty()) {
                    Toast.makeText(MainActivity.this, "Please Enter a String", Toast.LENGTH_SHORT).show();
                } else if (editText.getText().toString().isEmpty() == false) {
                    Toast.makeText(MainActivity.this, "Hello " + editText.getText().toString(), Toast.LENGTH_SHORT).show();
                }


            }
        });
    }
}
