# TF::FortiOS::LogThreatweight GeolocationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#country" title="Country">Country</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#level" title="Level">Level</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#country" title="Country">Country</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#level" title="Level">Level</a>: <i>String</i>
</pre>

## Properties

#### Country

Country code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

Entry ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

Threat weight score for Geolocation-based events. Valid values: `disable`, `low`, `medium`, `high`, `critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

