# TF::Splunk::OutputsTcpServer

Access data forwarding configurations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Splunk::OutputsTcpServer",
    "Properties" : {
        "<a href="#disabled" title="Disabled">Disabled</a>" : <i>Boolean</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sslaltnametocheck" title="SslAltNameToCheck">SslAltNameToCheck</a>" : <i>String</i>,
        "<a href="#sslcertpath" title="SslCertPath">SslCertPath</a>" : <i>String</i>,
        "<a href="#sslcipher" title="SslCipher">SslCipher</a>" : <i>String</i>,
        "<a href="#sslcommonnametocheck" title="SslCommonNameToCheck">SslCommonNameToCheck</a>" : <i>String</i>,
        "<a href="#sslpassword" title="SslPassword">SslPassword</a>" : <i>String</i>,
        "<a href="#sslrootcapath" title="SslRootCaPath">SslRootCaPath</a>" : <i>String</i>,
        "<a href="#sslverifyservercert" title="SslVerifyServerCert">SslVerifyServerCert</a>" : <i>Boolean</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ <a href="acldefinition.md">AclDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Splunk::OutputsTcpServer
Properties:
    <a href="#disabled" title="Disabled">Disabled</a>: <i>Boolean</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sslaltnametocheck" title="SslAltNameToCheck">SslAltNameToCheck</a>: <i>String</i>
    <a href="#sslcertpath" title="SslCertPath">SslCertPath</a>: <i>String</i>
    <a href="#sslcipher" title="SslCipher">SslCipher</a>: <i>String</i>
    <a href="#sslcommonnametocheck" title="SslCommonNameToCheck">SslCommonNameToCheck</a>: <i>String</i>
    <a href="#sslpassword" title="SslPassword">SslPassword</a>: <i>String</i>
    <a href="#sslrootcapath" title="SslRootCaPath">SslRootCaPath</a>: <i>String</i>
    <a href="#sslverifyservercert" title="SslVerifyServerCert">SslVerifyServerCert</a>: <i>Boolean</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - <a href="acldefinition.md">AclDefinition</a></i>
</pre>

## Properties

#### Disabled

If true, disables the group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Valid values: (clone | balance | autobalance)
The data distribution method used when two or more servers exist in the same forwarder group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

<host>:<port> of the Splunk receiver. <host> can be either an ip address or server name. <port> is the that port that the Splunk receiver is listening on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAltNameToCheck

The alternate name to match in the remote server's SSL certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertPath

Path to the client certificate. If specified, connection uses SSL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCipher

SSL Cipher in the form ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCommonNameToCheck

Check the common name of the server's certificate against this name.
If there is no match, assume that Splunk Enterprise is not authenticated against this server. You must specify this setting if sslVerifyServerCert is true.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPassword

The password associated with the CAcert.
The default Splunk Enterprise CAcert uses the password "password.".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslRootCaPath

The path to the root certificate authority file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslVerifyServerCert

If true, make sure that the server you are connecting to is a valid one (authenticated). Both the common name and the alternate name of the server are then checked for a match.

_Required_: No

_Type_: Boolean

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

