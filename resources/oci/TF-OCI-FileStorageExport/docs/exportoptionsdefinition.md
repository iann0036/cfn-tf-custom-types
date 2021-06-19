# TF::OCI::FileStorageExport ExportOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#anonymousgid" title="AnonymousGid">AnonymousGid</a>" : <i>String</i>,
    "<a href="#anonymousuid" title="AnonymousUid">AnonymousUid</a>" : <i>String</i>,
    "<a href="#identitysquash" title="IdentitySquash">IdentitySquash</a>" : <i>String</i>,
    "<a href="#requireprivilegedsourceport" title="RequirePrivilegedSourcePort">RequirePrivilegedSourcePort</a>" : <i>Boolean</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#anonymousgid" title="AnonymousGid">AnonymousGid</a>: <i>String</i>
<a href="#anonymousuid" title="AnonymousUid">AnonymousUid</a>: <i>String</i>
<a href="#identitysquash" title="IdentitySquash">IdentitySquash</a>: <i>String</i>
<a href="#requireprivilegedsourceport" title="RequirePrivilegedSourcePort">RequirePrivilegedSourcePort</a>: <i>Boolean</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### Access

(Updatable) Type of access to grant clients using the file system through this export. If unspecified defaults to `READ_ONLY`.
* `anonymous_gid` - (Optional) (Updatable) GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.
* `anonymous_uid` - (Optional) (Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `identity_squash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `require_privileged_source_port` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnonymousGid

(Updatable) GID value to remap to when squashing a client GID (see identitySquash for more details.) If unspecified defaults to `65534`.
* `anonymous_uid` - (Optional) (Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `identity_squash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `require_privileged_source_port` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnonymousUid

(Updatable) UID value to remap to when squashing a client UID (see identitySquash for more details.) If unspecified, defaults to `65534`.
* `identity_squash` - (Optional) (Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `require_privileged_source_port` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdentitySquash

(Updatable) Used when clients accessing the file system through this export have their UID and GID remapped to 'anonymousUid' and 'anonymousGid'. If `ALL`, all users and groups are remapped; if `ROOT`, only the root user and group (UID/GID 0) are remapped; if `NONE`, no remapping is done. If unspecified, defaults to `ROOT`.
* `require_privileged_source_port` - (Optional) (Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequirePrivilegedSourcePort

(Updatable) If `true`, clients accessing the file system through this export must connect from a privileged source port. If unspecified, defaults to `true`.
* `source` - (Required) (Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

(Updatable) Clients these options should apply to. Must be a either single IPv4 address or single IPv4 CIDR block.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

