# TF::Databricks::SqlPermissions

CloudFormation equivalent of databricks_sql_permissions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::SqlPermissions",
    "Properties" : {
        "<a href="#anonymousfunction" title="AnonymousFunction">AnonymousFunction</a>" : <i>Boolean</i>,
        "<a href="#anyfile" title="AnyFile">AnyFile</a>" : <i>Boolean</i>,
        "<a href="#catalog" title="Catalog">Catalog</a>" : <i>Boolean</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#database" title="Database">Database</a>" : <i>String</i>,
        "<a href="#table" title="Table">Table</a>" : <i>String</i>,
        "<a href="#view" title="View">View</a>" : <i>String</i>,
        "<a href="#privilegeassignments" title="PrivilegeAssignments">PrivilegeAssignments</a>" : <i>[ <a href="privilegeassignmentsdefinition.md">PrivilegeAssignmentsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::SqlPermissions
Properties:
    <a href="#anonymousfunction" title="AnonymousFunction">AnonymousFunction</a>: <i>Boolean</i>
    <a href="#anyfile" title="AnyFile">AnyFile</a>: <i>Boolean</i>
    <a href="#catalog" title="Catalog">Catalog</a>: <i>Boolean</i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#database" title="Database">Database</a>: <i>String</i>
    <a href="#table" title="Table">Table</a>: <i>String</i>
    <a href="#view" title="View">View</a>: <i>String</i>
    <a href="#privilegeassignments" title="PrivilegeAssignments">PrivilegeAssignments</a>: <i>
      - <a href="privilegeassignmentsdefinition.md">PrivilegeAssignmentsDefinition</a></i>
</pre>

## Properties

#### AnonymousFunction

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyFile

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Catalog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Table

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivilegeAssignments

_Required_: No

_Type_: List of <a href="privilegeassignmentsdefinition.md">PrivilegeAssignmentsDefinition</a>

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

