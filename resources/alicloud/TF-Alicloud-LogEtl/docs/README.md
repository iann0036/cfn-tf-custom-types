# TF::Alicloud::LogEtl

CloudFormation equivalent of alicloud_log_etl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::LogEtl",
    "Properties" : {
        "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
        "<a href="#accesskeysecret" title="AccessKeySecret">AccessKeySecret</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#etlname" title="EtlName">EtlName</a>" : <i>String</i>,
        "<a href="#etltype" title="EtlType">EtlType</a>" : <i>String</i>,
        "<a href="#fromtime" title="FromTime">FromTime</a>" : <i>Double</i>,
        "<a href="#kmsencryptedaccesskeyid" title="KmsEncryptedAccessKeyId">KmsEncryptedAccessKeyId</a>" : <i>String</i>,
        "<a href="#kmsencryptedaccesskeysecret" title="KmsEncryptedAccessKeySecret">KmsEncryptedAccessKeySecret</a>" : <i>String</i>,
        "<a href="#kmsencryptionaccesskeyidcontext" title="KmsEncryptionAccessKeyIdContext">KmsEncryptionAccessKeyIdContext</a>" : <i>[ <a href="kmsencryptionaccesskeyidcontextdefinition.md">KmsEncryptionAccessKeyIdContextDefinition</a>, ... ]</i>,
        "<a href="#kmsencryptionaccesskeysecretcontext" title="KmsEncryptionAccessKeySecretContext">KmsEncryptionAccessKeySecretContext</a>" : <i>[ <a href="kmsencryptionaccesskeysecretcontextdefinition.md">KmsEncryptionAccessKeySecretContextDefinition</a>, ... ]</i>,
        "<a href="#lastmodifiedtime" title="LastModifiedTime">LastModifiedTime</a>" : <i>Double</i>,
        "<a href="#logstore" title="Logstore">Logstore</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#schedule" title="Schedule">Schedule</a>" : <i>String</i>,
        "<a href="#script" title="Script">Script</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#totime" title="ToTime">ToTime</a>" : <i>Double</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#etlsinks" title="EtlSinks">EtlSinks</a>" : <i>[ <a href="etlsinksdefinition.md">EtlSinksDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::LogEtl
Properties:
    <a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
    <a href="#accesskeysecret" title="AccessKeySecret">AccessKeySecret</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#etlname" title="EtlName">EtlName</a>: <i>String</i>
    <a href="#etltype" title="EtlType">EtlType</a>: <i>String</i>
    <a href="#fromtime" title="FromTime">FromTime</a>: <i>Double</i>
    <a href="#kmsencryptedaccesskeyid" title="KmsEncryptedAccessKeyId">KmsEncryptedAccessKeyId</a>: <i>String</i>
    <a href="#kmsencryptedaccesskeysecret" title="KmsEncryptedAccessKeySecret">KmsEncryptedAccessKeySecret</a>: <i>String</i>
    <a href="#kmsencryptionaccesskeyidcontext" title="KmsEncryptionAccessKeyIdContext">KmsEncryptionAccessKeyIdContext</a>: <i>
      - <a href="kmsencryptionaccesskeyidcontextdefinition.md">KmsEncryptionAccessKeyIdContextDefinition</a></i>
    <a href="#kmsencryptionaccesskeysecretcontext" title="KmsEncryptionAccessKeySecretContext">KmsEncryptionAccessKeySecretContext</a>: <i>
      - <a href="kmsencryptionaccesskeysecretcontextdefinition.md">KmsEncryptionAccessKeySecretContextDefinition</a></i>
    <a href="#lastmodifiedtime" title="LastModifiedTime">LastModifiedTime</a>: <i>Double</i>
    <a href="#logstore" title="Logstore">Logstore</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#schedule" title="Schedule">Schedule</a>: <i>String</i>
    <a href="#script" title="Script">Script</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#totime" title="ToTime">ToTime</a>: <i>Double</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#etlsinks" title="EtlSinks">EtlSinks</a>: <i>
      - <a href="etlsinksdefinition.md">EtlSinksDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessKeySecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EtlName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EtlType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FromTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedAccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedAccessKeySecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionAccessKeyIdContext

_Required_: No

_Type_: List of <a href="kmsencryptionaccesskeyidcontextdefinition.md">KmsEncryptionAccessKeyIdContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptionAccessKeySecretContext

_Required_: No

_Type_: List of <a href="kmsencryptionaccesskeysecretcontextdefinition.md">KmsEncryptionAccessKeySecretContextDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastModifiedTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logstore

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Schedule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Script

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EtlSinks

_Required_: No

_Type_: List of <a href="etlsinksdefinition.md">EtlSinksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

