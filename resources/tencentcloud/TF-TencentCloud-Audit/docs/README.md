# TF::TencentCloud::Audit

Provides a resource to create an audit.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::Audit",
    "Properties" : {
        "<a href="#auditswitch" title="AuditSwitch">AuditSwitch</a>" : <i>Boolean</i>,
        "<a href="#cosbucket" title="CosBucket">CosBucket</a>" : <i>String</i>,
        "<a href="#cosregion" title="CosRegion">CosRegion</a>" : <i>String</i>,
        "<a href="#enablekmsencry" title="EnableKmsEncry">EnableKmsEncry</a>" : <i>Boolean</i>,
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#logfileprefix" title="LogFilePrefix">LogFilePrefix</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#readwriteattribute" title="ReadWriteAttribute">ReadWriteAttribute</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::Audit
Properties:
    <a href="#auditswitch" title="AuditSwitch">AuditSwitch</a>: <i>Boolean</i>
    <a href="#cosbucket" title="CosBucket">CosBucket</a>: <i>String</i>
    <a href="#cosregion" title="CosRegion">CosRegion</a>: <i>String</i>
    <a href="#enablekmsencry" title="EnableKmsEncry">EnableKmsEncry</a>: <i>Boolean</i>
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#logfileprefix" title="LogFilePrefix">LogFilePrefix</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#readwriteattribute" title="ReadWriteAttribute">ReadWriteAttribute</a>: <i>Double</i>
</pre>

## Properties

#### AuditSwitch

Indicate whether to turn on audit logging or not.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosBucket

Name of the cos bucket to save audit log. Caution: the validation of existing cos bucket will not be checked by terraform.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosRegion

Region of the cos bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableKmsEncry

Indicate whether the log is encrypt with KMS algorithm or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyId

Existing CMK unique key. This field can be get by data source `tencentcloud_audit_key_alias`. Caution: the region of the KMS must be as same as the `cos_region`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogFilePrefix

The log file name prefix. The length ranges from 3 to 40. If not set, the account ID will be the log file prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of audit. Valid length ranges from 3 to 128. Only alpha character or numbers or '_' supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadWriteAttribute

Event attribute filter. Valid values: `1`, `2`, `3`. `1` for readonly, `2` for write-only, `3` for all.

_Required_: Yes

_Type_: Double

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

