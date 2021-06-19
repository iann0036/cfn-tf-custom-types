# TF::Gridscale::Firewall

Provides a firewall resource. This can be used to create, modify, and delete firewalls.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gridscale::Firewall",
    "Properties" : {
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rulesv4in" title="RulesV4In">RulesV4In</a>" : <i>[ <a href="rulesv4indefinition.md">RulesV4InDefinition</a>, ... ]</i>,
        "<a href="#rulesv4out" title="RulesV4Out">RulesV4Out</a>" : <i>[ <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a>, ... ]</i>,
        "<a href="#rulesv6in" title="RulesV6In">RulesV6In</a>" : <i>[ <a href="rulesv6indefinition.md">RulesV6InDefinition</a>, ... ]</i>,
        "<a href="#rulesv6out" title="RulesV6Out">RulesV6Out</a>" : <i>[ <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gridscale::Firewall
Properties:
    <a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rulesv4in" title="RulesV4In">RulesV4In</a>: <i>
      - <a href="rulesv4indefinition.md">RulesV4InDefinition</a></i>
    <a href="#rulesv4out" title="RulesV4Out">RulesV4Out</a>: <i>
      - <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a></i>
    <a href="#rulesv6in" title="RulesV6In">RulesV6In</a>: <i>
      - <a href="rulesv6indefinition.md">RulesV6InDefinition</a></i>
    <a href="#rulesv6out" title="RulesV6Out">RulesV6Out</a>: <i>
      - <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Labels

List of labels in the format [ "label1", "label2" ].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The human-readable name of the object. It supports the full UTF-8 character set, with a maximum of 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV4In

_Required_: No

_Type_: List of <a href="rulesv4indefinition.md">RulesV4InDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV4Out

_Required_: No

_Type_: List of <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV6In

_Required_: No

_Type_: List of <a href="rulesv6indefinition.md">RulesV6InDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV6Out

_Required_: No

_Type_: List of <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ChangeTime

Returns the <code>ChangeTime</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### LocationName

Returns the <code>LocationName</code> value.

#### Network

Returns the <code>Network</code> value.

#### Private

Returns the <code>Private</code> value.

#### Status

Returns the <code>Status</code> value.

