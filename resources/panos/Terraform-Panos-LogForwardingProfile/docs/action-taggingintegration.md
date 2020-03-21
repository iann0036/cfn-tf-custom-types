# Terraform::Panos::LogForwardingProfile Action TaggingIntegration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#target" title="Target">Target</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>" : <i>[ &lt;a href=&#34;action-taggingintegration-localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;, ... ]</i>,
    "<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>" : <i>[ &lt;a href=&#34;action-taggingintegration-panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;, ... ]</i>,
    "<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>" : <i>[ &lt;a href=&#34;action-taggingintegration-remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#target" title="Target">Target</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>: <i>
      - &lt;a href=&#34;action-taggingintegration-localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;</i>
<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>: <i>
      - &lt;a href=&#34;action-taggingintegration-panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;</i>
<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>: <i>
      - &lt;a href=&#34;action-taggingintegration-remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;</i>
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
_Type_: List of &lt;a href=&#34;action-taggingintegration-localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaRegistration

_Required_: No
_Type_: List of &lt;a href=&#34;action-taggingintegration-panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteRegistration

_Required_: No
_Type_: List of &lt;a href=&#34;action-taggingintegration-remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

