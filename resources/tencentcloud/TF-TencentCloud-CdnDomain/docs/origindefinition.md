# TF::TencentCloud::CdnDomain OriginDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backuporiginlist" title="BackupOriginList">BackupOriginList</a>" : <i>[ String, ... ]</i>,
    "<a href="#backuporigintype" title="BackupOriginType">BackupOriginType</a>" : <i>String</i>,
    "<a href="#backupservername" title="BackupServerName">BackupServerName</a>" : <i>String</i>,
    "<a href="#cosprivateaccess" title="CosPrivateAccess">CosPrivateAccess</a>" : <i>String</i>,
    "<a href="#originlist" title="OriginList">OriginList</a>" : <i>[ String, ... ]</i>,
    "<a href="#originpullprotocol" title="OriginPullProtocol">OriginPullProtocol</a>" : <i>String</i>,
    "<a href="#origintype" title="OriginType">OriginType</a>" : <i>String</i>,
    "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backuporiginlist" title="BackupOriginList">BackupOriginList</a>: <i>
      - String</i>
<a href="#backuporigintype" title="BackupOriginType">BackupOriginType</a>: <i>String</i>
<a href="#backupservername" title="BackupServerName">BackupServerName</a>: <i>String</i>
<a href="#cosprivateaccess" title="CosPrivateAccess">CosPrivateAccess</a>: <i>String</i>
<a href="#originlist" title="OriginList">OriginList</a>: <i>
      - String</i>
<a href="#originpullprotocol" title="OriginPullProtocol">OriginPullProtocol</a>: <i>String</i>
<a href="#origintype" title="OriginType">OriginType</a>: <i>String</i>
<a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
</pre>

## Properties

#### BackupOriginList

Backup origin server list. Valid values can be ip or domain name. When modifying the backup origin server, you need to enter the corresponding `backup_origin_type`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupOriginType

Backup origin server type, which supports the following types: `domain`: domain name type, `ip`: IP list used as origin server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackupServerName

Host header used when accessing the backup origin server. If left empty, the ServerName of master origin server will be used by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CosPrivateAccess

When OriginType is COS, you can specify if access to private buckets is allowed. Valid values are `on` and `off`. and default value is `off`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginList

Master origin server list. Valid values can be ip or domain name. When modifying the origin server, you need to enter the corresponding `origin_type`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginPullProtocol

Origin-pull protocol configuration. `http`: forced HTTP origin-pull, `follow`: protocol follow origin-pull, `https`: forced HTTPS origin-pull. This only supports origin server port 443 for origin-pull.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginType

Master origin server type. The following types are supported: `domain`: domain name type, `cos`: COS origin, `ip`: IP list used as origin server, `ipv6`: origin server list is a single IPv6 address, `ip_ipv6`: origin server list is multiple IPv4 addresses and an IPv6 address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

Host header used when accessing the master origin server. If left empty, the acceleration domain name will be used by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

