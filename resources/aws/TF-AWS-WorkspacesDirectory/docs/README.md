# TF::AWS::WorkspacesDirectory

Provides a WorkSpaces directory in AWS WorkSpaces Service.

~> **NOTE:** AWS WorkSpaces service requires [`workspaces_DefaultRole`](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html#create-default-role) IAM role to operate normally.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::WorkspacesDirectory",
    "Properties" : {
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>String</i>,
        "<a href="#ipgroupids" title="IpGroupIds">IpGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#selfservicepermissions" title="SelfServicePermissions">SelfServicePermissions</a>" : <i>[ <a href="selfservicepermissionsdefinition.md">SelfServicePermissionsDefinition</a>, ... ]</i>,
        "<a href="#workspaceaccessproperties" title="WorkspaceAccessProperties">WorkspaceAccessProperties</a>" : <i>[ <a href="workspaceaccesspropertiesdefinition.md">WorkspaceAccessPropertiesDefinition</a>, ... ]</i>,
        "<a href="#workspacecreationproperties" title="WorkspaceCreationProperties">WorkspaceCreationProperties</a>" : <i>[ <a href="workspacecreationpropertiesdefinition.md">WorkspaceCreationPropertiesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::WorkspacesDirectory
Properties:
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>String</i>
    <a href="#ipgroupids" title="IpGroupIds">IpGroupIds</a>: <i>
      - String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#selfservicepermissions" title="SelfServicePermissions">SelfServicePermissions</a>: <i>
      - <a href="selfservicepermissionsdefinition.md">SelfServicePermissionsDefinition</a></i>
    <a href="#workspaceaccessproperties" title="WorkspaceAccessProperties">WorkspaceAccessProperties</a>: <i>
      - <a href="workspaceaccesspropertiesdefinition.md">WorkspaceAccessPropertiesDefinition</a></i>
    <a href="#workspacecreationproperties" title="WorkspaceCreationProperties">WorkspaceCreationProperties</a>: <i>
      - <a href="workspacecreationpropertiesdefinition.md">WorkspaceCreationPropertiesDefinition</a></i>
</pre>

## Properties

#### DirectoryId

The directory identifier for registration in WorkSpaces service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpGroupIds

The identifiers of the IP access control groups associated with the directory.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

The identifiers of the subnets where the directory resides.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelfServicePermissions

_Required_: No

_Type_: List of <a href="selfservicepermissionsdefinition.md">SelfServicePermissionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceAccessProperties

_Required_: No

_Type_: List of <a href="workspaceaccesspropertiesdefinition.md">WorkspaceAccessPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceCreationProperties

_Required_: No

_Type_: List of <a href="workspacecreationpropertiesdefinition.md">WorkspaceCreationPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Alias

Returns the <code>Alias</code> value.

#### CustomerUserName

Returns the <code>CustomerUserName</code> value.

#### DirectoryName

Returns the <code>DirectoryName</code> value.

#### DirectoryType

Returns the <code>DirectoryType</code> value.

#### DnsIpAddresses

Returns the <code>DnsIpAddresses</code> value.

#### IamRoleId

Returns the <code>IamRoleId</code> value.

#### Id

Returns the <code>Id</code> value.

#### RegistrationCode

Returns the <code>RegistrationCode</code> value.

#### WorkspaceSecurityGroupId

Returns the <code>WorkspaceSecurityGroupId</code> value.

