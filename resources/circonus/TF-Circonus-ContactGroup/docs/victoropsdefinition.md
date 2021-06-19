# TF::Circonus::ContactGroup VictoropsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apikey" title="ApiKey">ApiKey</a>" : <i>String</i>,
    "<a href="#contactgroupfallback" title="ContactGroupFallback">ContactGroupFallback</a>" : <i>String</i>,
    "<a href="#critical" title="Critical">Critical</a>" : <i>Double</i>,
    "<a href="#info" title="Info">Info</a>" : <i>Double</i>,
    "<a href="#team" title="Team">Team</a>" : <i>String</i>,
    "<a href="#warning" title="Warning">Warning</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#apikey" title="ApiKey">ApiKey</a>: <i>String</i>
<a href="#contactgroupfallback" title="ContactGroupFallback">ContactGroupFallback</a>: <i>String</i>
<a href="#critical" title="Critical">Critical</a>: <i>Double</i>
<a href="#info" title="Info">Info</a>: <i>Double</i>
<a href="#team" title="Team">Team</a>: <i>String</i>
<a href="#warning" title="Warning">Warning</a>: <i>Double</i>
</pre>

## Properties

#### ApiKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContactGroupFallback

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Critical

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Info

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Team

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

