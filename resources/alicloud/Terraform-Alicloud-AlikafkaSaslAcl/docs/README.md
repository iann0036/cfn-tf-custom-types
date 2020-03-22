# Terraform::Alicloud::AlikafkaSaslAcl

Provides an ALIKAFKA sasl acl resource.

-> **NOTE:** Available in 1.66.0+

-> **NOTE:**  Only the following regions support create alikafka sasl user.
[`cn-hangzhou`,`cn-beijing`,`cn-shenzhen`,`cn-shanghai`,`cn-qingdao`,`cn-hongkong`,`cn-huhehaote`,`cn-zhangjiakou`,`ap-southeast-1`,`ap-south-1`,`ap-southeast-5`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::AlikafkaSaslAcl",
    "Properties" : {
        "<a href="#acloperationtype" title="AclOperationType">AclOperationType</a>" : <i>String</i>,
        "<a href="#aclresourcename" title="AclResourceName">AclResourceName</a>" : <i>String</i>,
        "<a href="#aclresourcepatterntype" title="AclResourcePatternType">AclResourcePatternType</a>" : <i>String</i>,
        "<a href="#aclresourcetype" title="AclResourceType">AclResourceType</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::AlikafkaSaslAcl
Properties:
    <a href="#acloperationtype" title="AclOperationType">AclOperationType</a>: <i>String</i>
    <a href="#aclresourcename" title="AclResourceName">AclResourceName</a>: <i>String</i>
    <a href="#aclresourcepatterntype" title="AclResourcePatternType">AclResourcePatternType</a>: <i>String</i>
    <a href="#aclresourcetype" title="AclResourceType">AclResourceType</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### AclOperationType

Operation type for this acl. The operation type can only be "Write" and "Read".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourceName

Resource name for this acl. The resource name should be a topic or consumer group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourcePatternType

Resource pattern type for this acl. The resource pattern support two types "LITERAL" and "PREFIXED". "LITERAL": A literal name defines the full name of a resource. The special wildcard character "*" can be used to represent a resource with any name. "PREFIXED": A prefixed name defines a prefix for a resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AclResourceType

Resource type for this acl. The resource type can only be "Topic" and "Group".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

ID of the ALIKAFKA Instance that owns the groups.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username for the sasl user. The length should between 1 to 64 characters. The user should be an existed sasl user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Host

Returns the <code>Host</code> value.

#### Id

Returns the <code>Id</code> value.

