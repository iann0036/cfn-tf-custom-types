# TF::Volterra::FastAcl

CloudFormation equivalent of volterra_fast_acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::FastAcl",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#legacyacl" title="LegacyAcl">LegacyAcl</a>" : <i>[ <a href="legacyacldefinition.md">LegacyAclDefinition</a>, ... ]</i>,
        "<a href="#protocolpolicer" title="ProtocolPolicer">ProtocolPolicer</a>" : <i>[ <a href="protocolpolicerdefinition.md">ProtocolPolicerDefinition</a>, ... ]</i>,
        "<a href="#reacl" title="ReAcl">ReAcl</a>" : <i>[ <a href="reacldefinition.md">ReAclDefinition</a>, ... ]</i>,
        "<a href="#siteacl" title="SiteAcl">SiteAcl</a>" : <i>[ <a href="siteacldefinition.md">SiteAclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::FastAcl
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#legacyacl" title="LegacyAcl">LegacyAcl</a>: <i>
      - <a href="legacyacldefinition.md">LegacyAclDefinition</a></i>
    <a href="#protocolpolicer" title="ProtocolPolicer">ProtocolPolicer</a>: <i>
      - <a href="protocolpolicerdefinition.md">ProtocolPolicerDefinition</a></i>
    <a href="#reacl" title="ReAcl">ReAcl</a>: <i>
      - <a href="reacldefinition.md">ReAclDefinition</a></i>
    <a href="#siteacl" title="SiteAcl">SiteAcl</a>: <i>
      - <a href="siteacldefinition.md">SiteAclDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegacyAcl

_Required_: No

_Type_: List of <a href="legacyacldefinition.md">LegacyAclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPolicer

_Required_: No

_Type_: List of <a href="protocolpolicerdefinition.md">ProtocolPolicerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReAcl

_Required_: No

_Type_: List of <a href="reacldefinition.md">ReAclDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteAcl

_Required_: No

_Type_: List of <a href="siteacldefinition.md">SiteAclDefinition</a>

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
