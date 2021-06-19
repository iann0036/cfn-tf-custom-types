# TF::Databricks::Permissions

CloudFormation equivalent of databricks_permissions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::Permissions",
    "Properties" : {
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>String</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#clusterpolicyid" title="ClusterPolicyId">ClusterPolicyId</a>" : <i>String</i>,
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>String</i>,
        "<a href="#directorypath" title="DirectoryPath">DirectoryPath</a>" : <i>String</i>,
        "<a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>" : <i>String</i>,
        "<a href="#jobid" title="JobId">JobId</a>" : <i>String</i>,
        "<a href="#notebookid" title="NotebookId">NotebookId</a>" : <i>String</i>,
        "<a href="#notebookpath" title="NotebookPath">NotebookPath</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#sqlalertid" title="SqlAlertId">SqlAlertId</a>" : <i>String</i>,
        "<a href="#sqldashboardid" title="SqlDashboardId">SqlDashboardId</a>" : <i>String</i>,
        "<a href="#sqlendpointid" title="SqlEndpointId">SqlEndpointId</a>" : <i>String</i>,
        "<a href="#sqlqueryid" title="SqlQueryId">SqlQueryId</a>" : <i>String</i>,
        "<a href="#accesscontrol" title="AccessControl">AccessControl</a>" : <i>[ <a href="accesscontroldefinition.md">AccessControlDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::Permissions
Properties:
    <a href="#authorization" title="Authorization">Authorization</a>: <i>String</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#clusterpolicyid" title="ClusterPolicyId">ClusterPolicyId</a>: <i>String</i>
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>String</i>
    <a href="#directorypath" title="DirectoryPath">DirectoryPath</a>: <i>String</i>
    <a href="#instancepoolid" title="InstancePoolId">InstancePoolId</a>: <i>String</i>
    <a href="#jobid" title="JobId">JobId</a>: <i>String</i>
    <a href="#notebookid" title="NotebookId">NotebookId</a>: <i>String</i>
    <a href="#notebookpath" title="NotebookPath">NotebookPath</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#sqlalertid" title="SqlAlertId">SqlAlertId</a>: <i>String</i>
    <a href="#sqldashboardid" title="SqlDashboardId">SqlDashboardId</a>: <i>String</i>
    <a href="#sqlendpointid" title="SqlEndpointId">SqlEndpointId</a>: <i>String</i>
    <a href="#sqlqueryid" title="SqlQueryId">SqlQueryId</a>: <i>String</i>
    <a href="#accesscontrol" title="AccessControl">AccessControl</a>: <i>
      - <a href="accesscontroldefinition.md">AccessControlDefinition</a></i>
</pre>

## Properties

#### Authorization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterPolicyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectoryPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JobId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotebookId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotebookPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlAlertId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlDashboardId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlQueryId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessControl

_Required_: No

_Type_: List of <a href="accesscontroldefinition.md">AccessControlDefinition</a>

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

