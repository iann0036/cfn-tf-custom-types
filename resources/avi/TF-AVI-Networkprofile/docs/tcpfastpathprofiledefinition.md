# TF::AVI::Networkprofile TcpFastPathProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablesynprotection" title="EnableSynProtection">EnableSynProtection</a>" : <i>Boolean</i>,
    "<a href="#sessionidletimeout" title="SessionIdleTimeout">SessionIdleTimeout</a>" : <i>Double</i>,
    "<a href="#dsrprofile" title="DsrProfile">DsrProfile</a>" : <i>[ <a href="dsrprofiledefinition.md">DsrProfileDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enablesynprotection" title="EnableSynProtection">EnableSynProtection</a>: <i>Boolean</i>
<a href="#sessionidletimeout" title="SessionIdleTimeout">SessionIdleTimeout</a>: <i>Double</i>
<a href="#dsrprofile" title="DsrProfile">DsrProfile</a>: <i>
      - <a href="dsrprofiledefinition.md">DsrProfileDefinition</a></i>
</pre>

## Properties

#### EnableSynProtection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionIdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DsrProfile

_Required_: No

_Type_: List of <a href="dsrprofiledefinition.md">DsrProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

