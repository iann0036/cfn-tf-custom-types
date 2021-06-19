# TF::CheckPoint::ManagementBackupDomain

This command resource allows you to execute Check Point Backup Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementBackupDomain",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementBackupDomain
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
</pre>

## Properties

#### Domain

Domain can be identified by name or UID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePath

Path in which the backup domain data will be saved. <br>Should be the directory path or the full file path with ".tgz" <br>If no path was inserted the default will be: "/var/log/&lt;domain name&gt;_&lt;date&gt;.tgz".

_Required_: No

_Type_: String

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

#### TaskId

Returns the <code>TaskId</code> value.

