import jm.audio.io.*;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;
import jm.audio.Instrument;

/**
 * A basic additive synthesis instrument implementation
 * which implements different envelopes for odd and even harmonics
 * @author Andrew Brown
 */
public final class OddEvenInst extends Instrument{
	//----------------------------------------------
	// Attributes
	//----------------------------------------------
	/** the relative frequencies which make up this note */
	private float[] frequencies;
	/** the volumes to use for each frequency */
	private float[] volumes;	
	/** Pan */
	private float pan;
	/** The sample Rate to use */
	private int sampleRate;
	/** The Oscillators to use for each frequency specified */
	private Oscillator[] wt;
	/** The envelope to apply to each Oscillator's output */
	private Envelope[] env;
	/** The volume to apply to each envelopes output */
	private Volume[] vol;
	/** Stereo Pan Audio Object */
	private StereoPan[] span;

	private boolean header = true;
	private static int count = 0;
	private SampleOut sout;
	private int numberOfOvertones = 16;
	/** the envelope data */
        private EnvPoint[] pointArray0 = {
		new EnvPoint((float)0.0, (float)0.0),
		new EnvPoint((float)0.1, (float)1.0),
                new EnvPoint((float)0.4, (float)0.6),
		new EnvPoint((float)0.9, (float)0.3),
		new EnvPoint((float)1.0, (float)0.0)
	};
        
	private EnvPoint[] pointArray1 = {
		new EnvPoint((float)0.0, (float)0.0),
		new EnvPoint((float)0.1, (float)1.0),
		new EnvPoint((float)0.9, (float)0.1),
		new EnvPoint((float)1.0, (float)0.0)
	};
        
        private EnvPoint[] pointArray2 = {
		new EnvPoint((float)0.0, (float)0.0),
		new EnvPoint((float)0.1, (float)0.1),
		new EnvPoint((float)0.9, (float)1.0),
		new EnvPoint((float)1.0, (float)0.0)
	};
        
	//----------------------------------------------
	// Constructor
	//----------------------------------------------
	/**
	 * A simple constructor
	 * @param int sampleRate
	 */
	 public OddEvenInst(int sampleRate){
		//Provide some defaults
		this.sampleRate = sampleRate;
		this.frequencies = new float[numberOfOvertones];
		this.volumes = new float[numberOfOvertones];
	}
	/**
	 * A constructor that allows definition of the timbral complexity
	 */
	public OddEvenInst(int sampleRate, int numbOfOvertones){
		//Provide some defaults
		this.sampleRate = sampleRate;
		this.numberOfOvertones = numbOfOvertones;
		this.frequencies = new float[numberOfOvertones];
		this.volumes = new float[numberOfOvertones];
	}
	
	//----------------------------------------------
	// Methods 
	//----------------------------------------------
	/**
	 * Initialisation method is used to build the objects that
	 * this instrument will use
	 */
	public void createChain(){
		env = new Envelope[frequencies.length];
		vol = new Volume[frequencies.length];
		span = new StereoPan[frequencies.length];
		wt = new Oscillator[frequencies.length];
		for(int i=0; i < numberOfOvertones; i++){
			wt[i] = new Oscillator(this, Oscillator.SINE_WAVE,
                            this.sampleRate, 2);
			wt[i].setFrqRatio((float)i + 1);
                        // fundamental
                        if (i == 0) env[i] = new Envelope(wt[i], pointArray0);
                        // odd harmonics
                        if (i%2 == 0 && i != 0) {
                            env[i] = new Envelope(wt[i], pointArray1);
                            // even harmonics
                        } else {
                            if (i != 0) env[i] = new Envelope(wt[i], pointArray2);
                        }
			vol[i] = new Volume(env[i], (float)((1.0 / (i + 1)) * 1.5));
			span[i] = new StereoPan(vol[i], this.pan);
		}
		//And now the add object brings us back to one path.
		Add add = new Add(span);
		SampleOut sout = new SampleOut(add);
	}
}
