# TF::AWS::DirectoryServiceConditionalForwarder

Provides a conditional forwarder for managed Microsoft AD in AWS Directory Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DirectoryServiceConditionalForwarder",
    "Properties" : {
        "<a href="#directoryid" title="DirectoryId">DirectoryId</a>" : <i>String</i>,
        "<a href="#dnsips" title="DnsIps">DnsIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#remotedomainname" title="RemoteDomainName">RemoteDomainName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DirectoryServiceConditionalForwarder
Properties:
    <a href="#directoryid" title="DirectoryId">DirectoryId</a>: <i>String</i>
    <a href="#dnsips" title="DnsIps">DnsIps</a>: <i>
      - String</i>
    <a href="#remotedomainname" title="RemoteDomainName">RemoteDomainName</a>: <i>String</i>
</pre>

## Properties

#### DirectoryId

The id of directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsIps

A list of forwarder IP addresses.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteDomainName

The fully qualified domain name of the remote domain for which forwarders will be used.

_Required_: Yes

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

