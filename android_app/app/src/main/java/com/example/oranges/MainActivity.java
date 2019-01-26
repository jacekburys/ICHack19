package com.example.oranges;

import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentStatePagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity{

    private CameraFragment cameraFragment;
    private PhotoPageAdapter photoPageAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        photoPageAdapter = new PhotoPageAdapter(getSupportFragmentManager());
        ViewPager viewPager = findViewById(R.id.pager);
        viewPager.setAdapter(photoPageAdapter);

        cameraFragment = new CameraFragment();
    }


    public class PhotoPageAdapter extends FragmentStatePagerAdapter {
        public PhotoPageAdapter(FragmentManager fm) {
            super(fm);
        }

        @Override
        public Fragment getItem(int i) {
            if (i == 0) {
                return cameraFragment;
            }
            return null;
            /*
            else {
                return galleryFragment;
            }
            */
        }

        @Override
        public int getCount() {
            return 1;
        }

        @Override
        public CharSequence getPageTitle(int position) {
            return "OBJECT " + position;
        }
    }
}
