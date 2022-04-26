//==========================================================
// File:                 FractalInst.java
// Package:              inst
// Function:             Implementation of a fractal noise generator
// Author:               Andrew Brown
// Environment:          JDK1.1
//==========================================================
import jm.audio.io.*;
import jm.audio.synth.*;
import jm.audio.Instrument;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;

/**
 * A basic fractal noise synthesis instrument implementation
 * which implements envelope, pan, and volume control
 * @author Andrew Brown
 */

public class FractalInst extends Instrument{
	//----------------------------------------------
	// Attributes
	//----------------------------------------------
	
	/** The points to use in the construction of Envelopes */
	private EnvPoint[] pointArray = new EnvPoint[10];
	private int channels;
	private int sampleRate;
        private int resolution;

	//----------------------------------------------
	// Constructor
	//----------------------------------------------
	/**
	 * Basic default constructor to set an initial 
	 * sampling rate.
	 * @param sampleRate 
	 */
	public FractalInst(int sampleRate){
	    this(sampleRate, 1);
	}
	
	/**
	 * A second constructor to set an initial 
	 * sampling rate and number of channels.
	 * @param sampleRate 
	 * @param channels (i.e., 1 = mono, 2 = stereo)
	 */
	public FractalInst(int sampleRate, int channels){
            this(sampleRate, channels, 1);
        }
        
        /**
	 * A second constructor to set an initial 
	 * sampling rate and number of channels.
	 * @param sampleRate 
	 * @param channels (i.e., 1 = mono, 2 = stereo)
         * @param resolution the graininess of the fractal curve
	 */
	public FractalInst(int sampleRate, int channels, int res){
		this.sampleRate = sampleRate;
		this.channels = channels;
                this.resolution = res;
		EnvPoint[] tempArray = {
			new EnvPoint((float)0.0, (float)0.0),
			new EnvPoint((float)0.05, (float)1.0),
			new EnvPoint((float)0.15, (float)0.4),
			new EnvPoint((float)0.9, (float)0.3),
			new EnvPoint((float)1.0, (float)0.0)
		};
		pointArray = tempArray;
	}

	//----------------------------------------------
	// Methods 
	//----------------------------------------------
	   
	/**
	 * Initialisation method used to build a chain of the objects that
	 * this instrument will use.
	 */
	public void createChain(){
		Noise noise = new Noise(this, Noise.FRACTAL_NOISE, this.sampleRate);
		Envelope env = new Envelope(noise, pointArray);
		Volume vol = new Volume(env, (float)1.0);
		StereoPan span = new StereoPan(vol);
		SampleOut sout = new SampleOut(span);
	}	
}
