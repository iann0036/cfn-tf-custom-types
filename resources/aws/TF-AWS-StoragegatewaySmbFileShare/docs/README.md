# TF::AWS::StoragegatewaySmbFileShare

Manages an AWS Storage Gateway SMB File Share.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::StoragegatewaySmbFileShare",
    "Properties" : {
        "<a href="#accessbasedenumeration" title="AccessBasedEnumeration">AccessBasedEnumeration</a>" : <i>Boolean</i>,
        "<a href="#adminuserlist" title="AdminUserList">AdminUserList</a>" : <i>[ String, ... ]</i>,
        "<a href="#auditdestinationarn" title="AuditDestinationArn">AuditDestinationArn</a>" : <i>String</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
        "<a href="#casesensitivity" title="CaseSensitivity">CaseSensitivity</a>" : <i>String</i>,
        "<a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>" : <i>String</i>,
        "<a href="#filesharename" title="FileShareName">FileShareName</a>" : <i>String</i>,
        "<a href="#gatewayarn" title="GatewayArn">GatewayArn</a>" : <i>String</i>,
        "<a href="#guessmimetypeenabled" title="GuessMimeTypeEnabled">GuessMimeTypeEnabled</a>" : <i>Boolean</i>,
        "<a href="#invaliduserlist" title="InvalidUserList">InvalidUserList</a>" : <i>[ String, ... ]</i>,
        "<a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>" : <i>Boolean</i>,
        "<a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>" : <i>String</i>,
        "<a href="#locationarn" title="LocationArn">LocationArn</a>" : <i>String</i>,
        "<a href="#notificationpolicy" title="NotificationPolicy">NotificationPolicy</a>" : <i>String</i>,
        "<a href="#objectacl" title="ObjectAcl">ObjectAcl</a>" : <i>String</i>,
        "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
        "<a href="#requesterpays" title="RequesterPays">RequesterPays</a>" : <i>Boolean</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#smbaclenabled" title="SmbAclEnabled">SmbAclEnabled</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#validuserlist" title="ValidUserList">ValidUserList</a>" : <i>[ String, ... ]</i>,
        "<a href="#cacheattributes" title="CacheAttributes">CacheAttributes</a>" : <i>[ <a href="cacheattributesdefinition.md">CacheAttributesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::StoragegatewaySmbFileShare
Properties:
    <a href="#accessbasedenumeration" title="AccessBasedEnumeration">AccessBasedEnumeration</a>: <i>Boolean</i>
    <a href="#adminuserlist" title="AdminUserList">AdminUserList</a>: <i>
      - String</i>
    <a href="#auditdestinationarn" title="AuditDestinationArn">AuditDestinationArn</a>: <i>String</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
    <a href="#casesensitivity" title="CaseSensitivity">CaseSensitivity</a>: <i>String</i>
    <a href="#defaultstorageclass" title="DefaultStorageClass">DefaultStorageClass</a>: <i>String</i>
    <a href="#filesharename" title="FileShareName">FileShareName</a>: <i>String</i>
    <a href="#gatewayarn" title="GatewayArn">GatewayArn</a>: <i>String</i>
    <a href="#guessmimetypeenabled" title="GuessMimeTypeEnabled">GuessMimeTypeEnabled</a>: <i>Boolean</i>
    <a href="#invaliduserlist" title="InvalidUserList">InvalidUserList</a>: <i>
      - String</i>
    <a href="#kmsencrypted" title="KmsEncrypted">KmsEncrypted</a>: <i>Boolean</i>
    <a href="#kmskeyarn" title="KmsKeyArn">KmsKeyArn</a>: <i>String</i>
    <a href="#locationarn" title="LocationArn">LocationArn</a>: <i>String</i>
    <a href="#notificationpolicy" title="NotificationPolicy">NotificationPolicy</a>: <i>String</i>
    <a href="#objectacl" title="ObjectAcl">ObjectAcl</a>: <i>String</i>
    <a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
    <a href="#requesterpays" title="RequesterPays">RequesterPays</a>: <i>Boolean</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#smbaclenabled" title="SmbAclEnabled">SmbAclEnabled</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#validuserlist" title="ValidUserList">ValidUserList</a>: <i>
      - String</i>
    <a href="#cacheattributes" title="CacheAttributes">CacheAttributes</a>: <i>
      - <a href="cacheattributesdefinition.md">CacheAttributesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessBasedEnumeration

The files and folders on this share will only be visible to users with read access. Default value is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUserList

A list of users in the Active Directory that have admin access to the file share. Only valid if `authentication` is set to `ActiveDirectory`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditDestinationArn

The Amazon Resource Name (ARN) of the CloudWatch Log Group used for the audit logs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaseSensitivity

The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultStorageClass

The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileShareName

The name of the file share. Must be set if an S3 prefix name is set in `location_arn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayArn

Amazon Resource Name (ARN) of the file gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GuessMimeTypeEnabled

Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvalidUserList

A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncrypted

Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyArn

Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocationArn

The ARN of the backed storage used for storing file data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationPolicy

The notification policy of the file share. For more information see the [AWS Documentation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html#StorageGateway-CreateNFSFileShare-request-NotificationPolicy). Default value is `{}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectAcl

Access Control List permission for S3 bucket objects. Defaults to `private`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequesterPays

Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmbAclEnabled

Set this value to `true` to enable ACL (access control list) on the SMB fileshare. Set it to `false` to map file and directory permissions to the POSIX permissions. This setting applies only to `ActiveDirectory` authentication type.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidUserList

A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheAttributes

_Required_: No

_Type_: List of <a href="cacheattributesdefinition.md">CacheAttributesDefinition</a>

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

#### Arn

Returns the <code>Arn</code> value.

#### FileshareId

Returns the <code>FileshareId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Path

Returns the <code>Path</code> value.

