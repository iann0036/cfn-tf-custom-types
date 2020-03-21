# Terraform::Google::CloudRunDomainMapping Status

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ &lt;a href=&#34;status-conditions.md&#34;&gt;Conditions&lt;/a&gt;, ... ]</i>,
    "<a href="#mappedroutename" title="MappedRouteName">MappedRouteName</a>" : <i>String</i>,
    "<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>" : <i>Double</i>,
    "<a href="#resourcerecords" title="ResourceRecords">ResourceRecords</a>" : <i>[ &lt;a href=&#34;status-resourcerecords.md&#34;&gt;ResourceRecords&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#conditions" title="Conditions">Conditions</a>: <i>
      - &lt;a href=&#34;status-conditions.md&#34;&gt;Conditions&lt;/a&gt;</i>
<a href="#mappedroutename" title="MappedRouteName">MappedRouteName</a>: <i>String</i>
<a href="#observedgeneration" title="ObservedGeneration">ObservedGeneration</a>: <i>Double</i>
<a href="#resourcerecords" title="ResourceRecords">ResourceRecords</a>: <i>
      - &lt;a href=&#34;status-resourcerecords.md&#34;&gt;ResourceRecords&lt;/a&gt;</i>
</pre>

## Properties

#### Conditions

_Required_: No
_Type_: List of &lt;a href=&#34;status-conditions.md&#34;&gt;Conditions&lt;/a&gt;

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
_Type_: List of &lt;a href=&#34;status-resourcerecords.md&#34;&gt;ResourceRecords&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

