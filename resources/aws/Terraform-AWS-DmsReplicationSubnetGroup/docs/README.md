# Terraform::AWS::DmsReplicationSubnetGroup

Provides a DMS (Data Migration Service) replication subnet group resource. DMS replication subnet groups can be created, updated, deleted, and imported.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DmsReplicationSubnetGroup",
    "Properties" : {
        "<a href="#replicationsubnetgroupdescription" title="ReplicationSubnetGroupDescription">ReplicationSubnetGroupDescription</a>" : <i>String</i>,
        "<a href="#replicationsubnetgroupid" title="ReplicationSubnetGroupId">ReplicationSubnetGroupId</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DmsReplicationSubnetGroup
Properties:
    <a href="#replicationsubnetgroupdescription" title="ReplicationSubnetGroupDescription">ReplicationSubnetGroupDescription</a>: <i>String</i>
    <a href="#replicationsubnetgroupid" title="ReplicationSubnetGroupId">ReplicationSubnetGroupId</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### ReplicationSubnetGroupDescription

The description for the subnet group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplicationSubnetGroupId

The name for the replication subnet group. This value is stored as a lowercase string.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A list of the EC2 subnet IDs for the subnet group.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

#### ReplicationSubnetGroupArn

Returns the <code>ReplicationSubnetGroupArn</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

