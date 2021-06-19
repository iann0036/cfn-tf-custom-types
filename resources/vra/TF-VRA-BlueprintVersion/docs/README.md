# TF::VRA::BlueprintVersion

Creates a VMware vRealize Automation cloud template (blueprint) version resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::BlueprintVersion",
    "Properties" : {
        "<a href="#blueprintid" title="BlueprintId">BlueprintId</a>" : <i>String</i>,
        "<a href="#changelog" title="ChangeLog">ChangeLog</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#release" title="Release">Release</a>" : <i>Boolean</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::BlueprintVersion
Properties:
    <a href="#blueprintid" title="BlueprintId">BlueprintId</a>: <i>String</i>
    <a href="#changelog" title="ChangeLog">ChangeLog</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#release" title="Release">Release</a>: <i>Boolean</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### BlueprintId

ID of the cloud template  (blueprint).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChangeLog

Cloud template  (blueprint) version log.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-friendly description for the cloud template  (blueprint) version.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Release

Flag to indicate whether to release the version.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Cloud template  (blueprint) version.

_Required_: Yes

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

#### BlueprintDescription

Returns the <code>BlueprintDescription</code> value.

#### Content

Returns the <code>Content</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

#### ProjectId

Returns the <code>ProjectId</code> value.

#### ProjectName

Returns the <code>ProjectName</code> value.

#### Status

Returns the <code>Status</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### UpdatedBy

Returns the <code>UpdatedBy</code> value.

#### Valid

Returns the <code>Valid</code> value.

