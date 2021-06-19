# TF::ACI::FilterEntry

CloudFormation equivalent of aci_filter_entry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::FilterEntry",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#applytofrag" title="ApplyToFrag">ApplyToFrag</a>" : <i>String</i>,
        "<a href="#arpopc" title="ArpOpc">ArpOpc</a>" : <i>String</i>,
        "<a href="#dfromport" title="DFromPort">DFromPort</a>" : <i>String</i>,
        "<a href="#dtoport" title="DToPort">DToPort</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ethert" title="EtherT">EtherT</a>" : <i>String</i>,
        "<a href="#filterdn" title="FilterDn">FilterDn</a>" : <i>String</i>,
        "<a href="#icmpv4t" title="Icmpv4T">Icmpv4T</a>" : <i>String</i>,
        "<a href="#icmpv6t" title="Icmpv6T">Icmpv6T</a>" : <i>String</i>,
        "<a href="#matchdscp" title="MatchDscp">MatchDscp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#prot" title="Prot">Prot</a>" : <i>String</i>,
        "<a href="#sfromport" title="SFromPort">SFromPort</a>" : <i>String</i>,
        "<a href="#stoport" title="SToPort">SToPort</a>" : <i>String</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>String</i>,
        "<a href="#tcprules" title="TcpRules">TcpRules</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::FilterEntry
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#applytofrag" title="ApplyToFrag">ApplyToFrag</a>: <i>String</i>
    <a href="#arpopc" title="ArpOpc">ArpOpc</a>: <i>String</i>
    <a href="#dfromport" title="DFromPort">DFromPort</a>: <i>String</i>
    <a href="#dtoport" title="DToPort">DToPort</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ethert" title="EtherT">EtherT</a>: <i>String</i>
    <a href="#filterdn" title="FilterDn">FilterDn</a>: <i>String</i>
    <a href="#icmpv4t" title="Icmpv4T">Icmpv4T</a>: <i>String</i>
    <a href="#icmpv6t" title="Icmpv6T">Icmpv6T</a>: <i>String</i>
    <a href="#matchdscp" title="MatchDscp">MatchDscp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#prot" title="Prot">Prot</a>: <i>String</i>
    <a href="#sfromport" title="SFromPort">SFromPort</a>: <i>String</i>
    <a href="#stoport" title="SToPort">SToPort</a>: <i>String</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>String</i>
    <a href="#tcprules" title="TcpRules">TcpRules</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyToFrag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArpOpc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DFromPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DToPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EtherT

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv4T

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Icmpv6T

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchDscp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SFromPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SToPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TcpRules

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

