# Terraform::Panos::PanoramaLogForwardingProfile TaggingIntegration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>" : <i>[ <a href="taggingintegration-localregistration.md">LocalRegistration</a>, ... ]</i>,
    "<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>" : <i>[ <a href="taggingintegration-panoramaregistration.md">PanoramaRegistration</a>, ... ]</i>,
    "<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>" : <i>[ <a href="taggingintegration-remoteregistration.md">RemoteRegistration</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>: <i>
      - <a href="taggingintegration-localregistration.md">LocalRegistration</a></i>
<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>: <i>
      - <a href="taggingintegration-panoramaregistration.md">PanoramaRegistration</a></i>
<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>: <i>
      - <a href="taggingintegration-remoteregistration.md">RemoteRegistration</a></i>
</pre>

## Properties

#### Action

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Target

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRegistration

_Required_: No
_Type_: List of <a href="taggingintegration-localregistration.md">LocalRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaRegistration

_Required_: No
_Type_: List of <a href="taggingintegration-panoramaregistration.md">PanoramaRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteRegistration

_Required_: No
_Type_: List of <a href="taggingintegration-remoteregistration.md">RemoteRegistration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

