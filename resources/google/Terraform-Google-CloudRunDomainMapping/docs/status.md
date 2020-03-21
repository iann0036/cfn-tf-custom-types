# Terraform::Google::CloudRunDomainMapping Status

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="status-conditions.md">Conditions</a>, ... ]</i>,
    "<a href="#mappedroutename" title="MappedRouteName">MappedRouteName</a>" : <i>String</i>,
    "<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>" : <i>Double</i>,
    "<a href="#resourcerecords" title="ResourceRecords">ResourceRecords</a>" : <i>[ <a href="status-resourcerecords.md">ResourceRecords</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="status-conditions.md">Conditions</a></i>
<a href="#mappedroutename" title="MappedRouteName">MappedRouteName</a>: <i>String</i>
<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>: <i>Double</i>
<a href="#resourcerecords" title="ResourceRecords">ResourceRecords</a>: <i>
      - <a href="status-resourcerecords.md">ResourceRecords</a></i>
</pre>

## Properties

#### Conditions

_Required_: No

_Type_: List of <a href="status-conditions.md">Conditions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MappedRouteName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObservedGeneration

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceRecords

_Required_: No

_Type_: List of <a href="status-resourcerecords.md">ResourceRecords</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

