# TF::CheckPoint::ManagementRestoreDomain

This command resource allows you to execute Check Point Restore Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementRestoreDomain",
    "Properties" : {
        "<a href="#domainipaddress" title="DomainIpAddress">DomainIpAddress</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#domainservername" title="DomainServerName">DomainServerName</a>" : <i>String</i>,
        "<a href="#filepath" title="FilePath">FilePath</a>" : <i>String</i>,
        "<a href="#verifyonly" title="VerifyOnly">VerifyOnly</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementRestoreDomain
Properties:
    <a href="#domainipaddress" title="DomainIpAddress">DomainIpAddress</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#domainservername" title="DomainServerName">DomainServerName</a>: <i>String</i>
    <a href="#filepath" title="FilePath">FilePath</a>: <i>String</i>
    <a href="#verifyonly" title="VerifyOnly">VerifyOnly</a>: <i>Boolean</i>
</pre>

## Properties

#### DomainIpAddress

IPv4 address.<br><font color="red">Required only for</font> importing Security Management Server into Multi-Domain Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

Domain name. Should be unique in the MDS.<br><font color="red">Required only for</font> importing Security Management Server into Multi-Domain Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainServerName

Multi Domain server name.<br><font color="red">Required only for</font> importing Security Management Server into Multi-Domain Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilePath

Path to the backup file to be restored. <br>Should be the full file path (example, "/var/log/domain1_backup.tgz").

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyOnly

If true, verify that the import operation is valid for this input file and this environment <br>Note: Restore operation will not be executed.

_Required_: No

_Type_: Boolean

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

Asynchronous task unique identifier.

