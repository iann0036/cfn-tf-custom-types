# TF::Google::BigtableTable

Creates a Google Cloud Bigtable table inside an instance. For more information see
[the official documentation](https://cloud.google.com/bigtable/) and
[API](https://cloud.google.com/bigtable/docs/go/reference).

-> **Note:** It is strongly recommended to set `lifecycle { prevent_destroy = true }`
on tables in order to prevent accidental data loss. See
[Terraform docs](https://www.terraform.io/docs/configuration/resources.html#prevent_destroy)
for more information on lifecycle parameters.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::BigtableTable",
    "Properties" : {
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#splitkeys" title="SplitKeys">SplitKeys</a>" : <i>[ String, ... ]</i>,
        "<a href="#columnfamily" title="ColumnFamily">ColumnFamily</a>" : <i>[ <a href="columnfamilydefinition.md">ColumnFamilyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::BigtableTable
Properties:
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#splitkeys" title="SplitKeys">SplitKeys</a>: <i>
      - String</i>
    <a href="#columnfamily" title="ColumnFamily">ColumnFamily</a>: <i>
      - <a href="columnfamilydefinition.md">ColumnFamilyDefinition</a></i>
</pre>

## Properties

#### InstanceName

The name of the Bigtable instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the table.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitKeys

A list of predefined keys to split the table on.
!> **Warning:** Modifying the `split_keys` of an existing table will cause Terraform
to delete/recreate the entire `google_bigtable_table` resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ColumnFamily

_Required_: No

_Type_: List of <a href="columnfamilydefinition.md">ColumnFamilyDefinition</a>

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

