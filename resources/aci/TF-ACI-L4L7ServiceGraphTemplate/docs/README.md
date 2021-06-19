# TF::ACI::L4L7ServiceGraphTemplate

CloudFormation equivalent of aci_l4_l7_service_graph_template

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::L4L7ServiceGraphTemplate",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#l4l7servicegraphtemplatetype" title="L4L7ServiceGraphTemplateType">L4L7ServiceGraphTemplateType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>,
        "<a href="#termconsdn" title="TermConsDn">TermConsDn</a>" : <i>String</i>,
        "<a href="#termconsname" title="TermConsName">TermConsName</a>" : <i>String</i>,
        "<a href="#termnodeconsdn" title="TermNodeConsDn">TermNodeConsDn</a>" : <i>String</i>,
        "<a href="#termnodeprovdn" title="TermNodeProvDn">TermNodeProvDn</a>" : <i>String</i>,
        "<a href="#termprovdn" title="TermProvDn">TermProvDn</a>" : <i>String</i>,
        "<a href="#termprovname" title="TermProvName">TermProvName</a>" : <i>String</i>,
        "<a href="#uitemplatetype" title="UiTemplateType">UiTemplateType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::L4L7ServiceGraphTemplate
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#l4l7servicegraphtemplatetype" title="L4L7ServiceGraphTemplateType">L4L7ServiceGraphTemplateType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
    <a href="#termconsdn" title="TermConsDn">TermConsDn</a>: <i>String</i>
    <a href="#termconsname" title="TermConsName">TermConsName</a>: <i>String</i>
    <a href="#termnodeconsdn" title="TermNodeConsDn">TermNodeConsDn</a>: <i>String</i>
    <a href="#termnodeprovdn" title="TermNodeProvDn">TermNodeProvDn</a>: <i>String</i>
    <a href="#termprovdn" title="TermProvDn">TermProvDn</a>: <i>String</i>
    <a href="#termprovname" title="TermProvName">TermProvName</a>: <i>String</i>
    <a href="#uitemplatetype" title="UiTemplateType">UiTemplateType</a>: <i>String</i>
</pre>

## Properties

#### Annotation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### L4L7ServiceGraphTemplateType

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

#### TenantDn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermConsDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermConsName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermNodeConsDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermNodeProvDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermProvDn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TermProvName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UiTemplateType

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

