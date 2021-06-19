# TF::FortiOS::SystemClustersync SessionSyncFilterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>String</i>,
    "<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>" : <i>String</i>,
    "<a href="#dstintf" title="Dstintf">Dstintf</a>" : <i>String</i>,
    "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>String</i>,
    "<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>" : <i>String</i>,
    "<a href="#srcintf" title="Srcintf">Srcintf</a>" : <i>String</i>,
    "<a href="#customservice" title="CustomService">CustomService</a>" : <i>[ <a href="customservicedefinition.md">CustomServiceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>String</i>
<a href="#dstaddr6" title="Dstaddr6">Dstaddr6</a>: <i>String</i>
<a href="#dstintf" title="Dstintf">Dstintf</a>: <i>String</i>
<a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>String</i>
<a href="#srcaddr6" title="Srcaddr6">Srcaddr6</a>: <i>String</i>
<a href="#srcintf" title="Srcintf">Srcintf</a>: <i>String</i>
<a href="#customservice" title="CustomService">CustomService</a>: <i>
      - <a href="customservicedefinition.md">CustomServiceDefinition</a></i>
</pre>

## Properties

#### Dstaddr

Only sessions to this IPv4 address are synchronized. You can only enter one address. To synchronize sessions for multiple destination addresses, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr6

Only sessions to this IPv6 address are synchronized. You can only enter one address. To synchronize sessions for multiple destination addresses, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstintf

Only sessions to this interface are synchronized. You can only enter one interface name. To synchronize sessions to multiple destination interfaces, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

Only sessions from this IPv4 address are synchronized. You can only enter one address. To synchronize sessions from multiple source addresses, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr6

Only sessions from this IPv6 address are synchronized. You can only enter one address. To synchronize sessions from multiple source addresses, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcintf

Only sessions from this interface are synchronized. You can only enter one interface name. To synchronize sessions for multiple source interfaces, add multiple filters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomService

_Required_: No

_Type_: List of <a href="customservicedefinition.md">CustomServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

