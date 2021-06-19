# TF::Alkira::ConnectorIpsec AdvancedDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dpddelay" title="DpdDelay">DpdDelay</a>" : <i>String</i>,
    "<a href="#dpdtimeout" title="DpdTimeout">DpdTimeout</a>" : <i>String</i>,
    "<a href="#espdhgroupnumbers" title="EspDhGroupNumbers">EspDhGroupNumbers</a>" : <i>String</i>,
    "<a href="#espencryptionalgorithms" title="EspEncryptionAlgorithms">EspEncryptionAlgorithms</a>" : <i>String</i>,
    "<a href="#espintegrityalgorithms" title="EspIntegrityAlgorithms">EspIntegrityAlgorithms</a>" : <i>String</i>,
    "<a href="#esplifetime" title="EspLifeTime">EspLifeTime</a>" : <i>Double</i>,
    "<a href="#esprandomtime" title="EspRandomTime">EspRandomTime</a>" : <i>String</i>,
    "<a href="#esprekeytime" title="EspRekeyTime">EspRekeyTime</a>" : <i>String</i>,
    "<a href="#ikedhgroupnumbers" title="IkeDhGroupNumbers">IkeDhGroupNumbers</a>" : <i>String</i>,
    "<a href="#ikeencryptionalgorithms" title="IkeEncryptionAlgorithms">IkeEncryptionAlgorithms</a>" : <i>String</i>,
    "<a href="#ikeintegrityalgorithms" title="IkeIntegrityAlgorithms">IkeIntegrityAlgorithms</a>" : <i>String</i>,
    "<a href="#ikeovertime" title="IkeOverTime">IkeOverTime</a>" : <i>Double</i>,
    "<a href="#ikerandomtime" title="IkeRandomTime">IkeRandomTime</a>" : <i>Double</i>,
    "<a href="#ikerekeytime" title="IkeRekeyTime">IkeRekeyTime</a>" : <i>Double</i>,
    "<a href="#ikeversion" title="IkeVersion">IkeVersion</a>" : <i>String</i>,
    "<a href="#initiator" title="Initiator">Initiator</a>" : <i>String</i>,
    "<a href="#localauthtype" title="LocalAuthType">LocalAuthType</a>" : <i>String</i>,
    "<a href="#localauthvalue" title="LocalAuthValue">LocalAuthValue</a>" : <i>String</i>,
    "<a href="#remoteauthtype" title="RemoteAuthType">RemoteAuthType</a>" : <i>String</i>,
    "<a href="#remoteauthvalue" title="RemoteAuthValue">RemoteAuthValue</a>" : <i>String</i>,
    "<a href="#replaywindowsize" title="ReplayWindowSize">ReplayWindowSize</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#dpddelay" title="DpdDelay">DpdDelay</a>: <i>String</i>
<a href="#dpdtimeout" title="DpdTimeout">DpdTimeout</a>: <i>String</i>
<a href="#espdhgroupnumbers" title="EspDhGroupNumbers">EspDhGroupNumbers</a>: <i>String</i>
<a href="#espencryptionalgorithms" title="EspEncryptionAlgorithms">EspEncryptionAlgorithms</a>: <i>String</i>
<a href="#espintegrityalgorithms" title="EspIntegrityAlgorithms">EspIntegrityAlgorithms</a>: <i>String</i>
<a href="#esplifetime" title="EspLifeTime">EspLifeTime</a>: <i>Double</i>
<a href="#esprandomtime" title="EspRandomTime">EspRandomTime</a>: <i>String</i>
<a href="#esprekeytime" title="EspRekeyTime">EspRekeyTime</a>: <i>String</i>
<a href="#ikedhgroupnumbers" title="IkeDhGroupNumbers">IkeDhGroupNumbers</a>: <i>String</i>
<a href="#ikeencryptionalgorithms" title="IkeEncryptionAlgorithms">IkeEncryptionAlgorithms</a>: <i>String</i>
<a href="#ikeintegrityalgorithms" title="IkeIntegrityAlgorithms">IkeIntegrityAlgorithms</a>: <i>String</i>
<a href="#ikeovertime" title="IkeOverTime">IkeOverTime</a>: <i>Double</i>
<a href="#ikerandomtime" title="IkeRandomTime">IkeRandomTime</a>: <i>Double</i>
<a href="#ikerekeytime" title="IkeRekeyTime">IkeRekeyTime</a>: <i>Double</i>
<a href="#ikeversion" title="IkeVersion">IkeVersion</a>: <i>String</i>
<a href="#initiator" title="Initiator">Initiator</a>: <i>String</i>
<a href="#localauthtype" title="LocalAuthType">LocalAuthType</a>: <i>String</i>
<a href="#localauthvalue" title="LocalAuthValue">LocalAuthValue</a>: <i>String</i>
<a href="#remoteauthtype" title="RemoteAuthType">RemoteAuthType</a>: <i>String</i>
<a href="#remoteauthvalue" title="RemoteAuthValue">RemoteAuthValue</a>: <i>String</i>
<a href="#replaywindowsize" title="ReplayWindowSize">ReplayWindowSize</a>: <i>Double</i>
</pre>

## Properties

#### DpdDelay

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpdTimeout

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspDhGroupNumbers

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspEncryptionAlgorithms

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspIntegrityAlgorithms

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspLifeTime

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspRandomTime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspRekeyTime

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeDhGroupNumbers

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeEncryptionAlgorithms

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeIntegrityAlgorithms

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeOverTime

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRandomTime

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeRekeyTime

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeVersion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initiator

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAuthType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalAuthValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAuthType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteAuthValue

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplayWindowSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

