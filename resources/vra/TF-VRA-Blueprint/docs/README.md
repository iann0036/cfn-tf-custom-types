# TF::VRA::Blueprint

Creates a VMware vRealize Automation (vRA) cloud template resource, formerly known as a blueprint.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VRA::Blueprint",
    "Properties" : {
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#requestscopeorg" title="RequestScopeOrg">RequestScopeOrg</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::VRA::Blueprint
Properties:
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#requestscopeorg" title="RequestScopeOrg">RequestScopeOrg</a>: <i>Boolean</i>
</pre>

## Properties

#### Content

Blueprint YAML content.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Human-friendly description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Human-friendly name used as an identifier in APIs that support this option.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of project that entity belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestScopeOrg

Flag to indicate whether blueprint can be requested from any project in the organization that entity belongs to.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ContentSourceId

Returns the <code>ContentSourceId</code> value.

#### ContentSourcePath

Returns the <code>ContentSourcePath</code> value.

#### ContentSourceSyncAt

Returns the <code>ContentSourceSyncAt</code> value.

#### ContentSourceSyncMessages

Returns the <code>ContentSourceSyncMessages</code> value.

#### ContentSourceSyncStatus

Returns the <code>ContentSourceSyncStatus</code> value.

#### ContentSourceType

Returns the <code>ContentSourceType</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### CreatedBy

Returns the <code>CreatedBy</code> value.

#### Id

Returns the <code>Id</code> value.

#### OrgId

Returns the <code>OrgId</code> value.

#### ProjectName

Returns the <code>ProjectName</code> value.

#### SelfLink

Returns the <code>SelfLink</code> value.

#### Status

Returns the <code>Status</code> value.

#### TotalReleasedVersions

Returns the <code>TotalReleasedVersions</code> value.

#### TotalVersions

Returns the <code>TotalVersions</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

#### UpdatedBy

Returns the <code>UpdatedBy</code> value.

#### Valid

Returns the <code>Valid</code> value.

#### ValidationMessages

Returns the <code>ValidationMessages</code> value.

