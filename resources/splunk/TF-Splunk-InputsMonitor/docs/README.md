# TF::Splunk::InputsMonitor

Create or update a new file or directory monitor input.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::InputsMonitor",
    "Properties" : {
        "<a href="#blacklist" title="Blacklist">Blacklist</a>" : <i>String</i>,
        "<a href="#crcsalt" title="CrcSalt">CrcSalt</a>" : <i>String</i>,
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#followtail" title="FollowTail">FollowTail</a>" : <i>Boolean</i>,
        "<a href="#host" title="Host">Host</a>" : <i>String</i>,
        "<a href="#hostregex" title="HostRegex">HostRegex</a>" : <i>String</i>,
        "<a href="#hostsegment" title="HostSegment">HostSegment</a>" : <i>Double</i>,
        "<a href="#ignoreolderthan" title="IgnoreOlderThan">IgnoreOlderThan</a>" : <i>String</i>,
        "<a href="#index" title="Index">Index</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recursive" title="Recursive">Recursive</a>" : <i>Boolean</i>,
        "<a href="#renamesource" title="RenameSource">RenameSource</a>" : <i>String</i>,
        "<a href="#sourcetype" title="Sourcetype">Sourcetype</a>" : <i>String</i>,
        "<a href="#timebeforeclose" title="TimeBeforeClose">TimeBeforeClose</a>" : <i>Double</i>,
        "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::InputsMonitor
Properties:
    <a href="#blacklist" title="Blacklist">Blacklist</a>: <i>String</i>
    <a href="#crcsalt" title="CrcSalt">CrcSalt</a>: <i>String</i>
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#followtail" title="FollowTail">FollowTail</a>: <i>Boolean</i>
    <a href="#host" title="Host">Host</a>: <i>String</i>
    <a href="#hostregex" title="HostRegex">HostRegex</a>: <i>String</i>
    <a href="#hostsegment" title="HostSegment">HostSegment</a>: <i>Double</i>
    <a href="#ignoreolderthan" title="IgnoreOlderThan">IgnoreOlderThan</a>: <i>String</i>
    <a href="#index" title="Index">Index</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recursive" title="Recursive">Recursive</a>: <i>Boolean</i>
    <a href="#renamesource" title="RenameSource">RenameSource</a>: <i>String</i>
    <a href="#sourcetype" title="Sourcetype">Sourcetype</a>: <i>String</i>
    <a href="#timebeforeclose" title="TimeBeforeClose">TimeBeforeClose</a>: <i>Double</i>
    <a href="#whitelist" title="Whitelist">Whitelist</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### Blacklist

Specify a regular expression for a file path. The file path that matches this regular expression is not indexed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrcSalt

A string that modifies the file tracking identity for files in this input. The magic value <SOURCE> invokes special behavior.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disabled

Indicates if input monitoring is disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowTail

If set to true, files that are seen for the first time is read from the end.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

The value to populate in the host field for events from this data input.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRegex

Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSegment

Use the specified slash-separate segment of the filepath as the host field value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreOlderThan

Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

Which index events from this input should be stored in. Defaults to default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The file or directory path to monitor on the system.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recursive

Setting this to false prevents monitoring of any subdirectories encountered within this data input.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenameSource

The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sourcetype

The value to populate in the sourcetype field for incoming events.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeBeforeClose

When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

Specify a regular expression for a file path. Only file paths that match this regular expression are indexed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of <a href="acldefinition.md">AclDefinition</a>

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

