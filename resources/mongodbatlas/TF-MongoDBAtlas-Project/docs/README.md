# TF::MongoDBAtlas::Project

`mongodbatlas_project` provides a Project resource. This allows project to be created.

~> **IMPORTANT WARNING:**  Changing the name of an existing Project in your Terraform configuration will result the destruction of that Project and related resources (including Clusters) and the re-creation of those resources.  Terraform will inform you of the destroyed/created resources before applying so be sure to verify any change to your environment before applying.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::MongoDBAtlas::Project",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#orgid" title="OrgId">OrgId</a>" : <i>String</i>,
        "<a href="#teams" title="Teams">Teams</a>" : <i>[ <a href="teamsdefinition.md">TeamsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::MongoDBAtlas::Project
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#orgid" title="OrgId">OrgId</a>: <i>String</i>
    <a href="#teams" title="Teams">Teams</a>: <i>
      - <a href="teamsdefinition.md">TeamsDefinition</a></i>
</pre>

## Properties

#### Name

The name of the project you want to create. (Cannot be changed via this Provider after creation.).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgId

The ID of the organization you want to create the project within.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Teams

_Required_: No

_Type_: List of <a href="teamsdefinition.md">TeamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClusterCount

Returns the <code>ClusterCount</code> value.

#### Created

Returns the <code>Created</code> value.

#### Id

Returns the <code>Id</code> value.

