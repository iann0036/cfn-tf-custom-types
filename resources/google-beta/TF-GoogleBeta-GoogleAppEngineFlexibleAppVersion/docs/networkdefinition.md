# TF::GoogleBeta::GoogleAppEngineFlexibleAppVersion NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forwardedports" title="ForwardedPorts">ForwardedPorts</a>" : <i>[ String, ... ]</i>,
    "<a href="#instancetag" title="InstanceTag">InstanceTag</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>" : <i>Boolean</i>,
    "<a href="#subnetwork" title="Subnetwork">Subnetwork</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#forwardedports" title="ForwardedPorts">ForwardedPorts</a>: <i>
      - String</i>
<a href="#instancetag" title="InstanceTag">InstanceTag</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#sessionaffinity" title="SessionAffinity">SessionAffinity</a>: <i>Boolean</i>
<a href="#subnetwork" title="Subnetwork">Subnetwork</a>: <i>String</i>
</pre>

## Properties

#### ForwardedPorts

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionAffinity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnetwork

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

