
import jm.audio.Instrument;
import jm.audio.io.*;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;

/**
 * A basic pulsewave waveform instrument implementation
 * which implements envelope , pan, and volume control
 * @author Andrew Brown and Andrew Sorensen
 */

public final class PulsewaveInst extends Instrument{
	//----------------------------------------------
	// Attributes
	//----------------------------------------------
	
	/** The points to use in the construction of Envelopes */
	private EnvPoint[] pointArray = new EnvPoint[10];
	private int sampleRate;
    private SampleOut sout;

	//----------------------------------------------
	// Constructor
	//----------------------------------------------
	/**
	 * Basic default constructor to set an initial 
	 * sampling rate and buffersize in addition
	 * to the neccessary frequency relationships 
	 * and volumes for each frequency to be added
	 * the instrument
	 * @param sampleRate 
	 * @param buffersize
	 * @param frequencies the relative freqencies to use
	 * @param volumes the volumes to use for the frequencies
	 */
	public PulsewaveInst(int sampleRate){
		this.sampleRate = sampleRate;
		EnvPoint[] tempArray = {
			new EnvPoint((float)0.0, (float)0.0),
			new EnvPoint((float)0.02, (float)1.0),
			new EnvPoint((float)0.15, (float)0.6),
			new EnvPoint((float)0.9, (float)0.3),
			new EnvPoint((float)1.0, (float)0.0)
		};
		pointArray = tempArray;
	}

	//----------------------------------------------
	// Methods 
	//----------------------------------------------
	   
	/**
	 * Initialisation method used to build the objects that
	 * this instrument will use
	 */
	public void createChain(){
		Oscillator wt = new Oscillator(this, Oscillator.PULSE_WAVE, 
                    this.sampleRate, 2);
                wt.setPulseWidth(0.15);
		Envelope env = new Envelope(wt, pointArray);
		Volume vol = new Volume(env);
		StereoPan span = new StereoPan(vol);
		if(output == RENDER) sout = new SampleOut(span);
	}	
}

