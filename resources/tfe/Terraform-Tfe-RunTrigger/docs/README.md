# Terraform::Tfe::RunTrigger

Terraform Cloud provides a way to connect your workspace to one or more workspaces within your organization, known as "source workspaces". 
These connections, called run triggers, allow runs to queue automatically in your workspace on successful apply of runs in any of the source workspaces. 
You can connect your workspace to up to 20 source workspaces.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Tfe::RunTrigger",
    "Properties" : {
        "<a href="#sourceableid" title="SourceableId">SourceableId</a>" : <i>String</i>,
        "<a href="#workspaceexternalid" title="WorkspaceExternalId">WorkspaceExternalId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Tfe::RunTrigger
Properties:
    <a href="#sourceableid" title="SourceableId">SourceableId</a>: <i>String</i>
    <a href="#workspaceexternalid" title="WorkspaceExternalId">WorkspaceExternalId</a>: <i>String</i>
</pre>

## Properties

#### SourceableId

The external id of the sourceable. The sourceable must be a workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceExternalId

The external id of the workspace that owns the run trigger. This is the workspace where runs will be triggered.

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

#### Id

Returns the <code>Id</code> value.

