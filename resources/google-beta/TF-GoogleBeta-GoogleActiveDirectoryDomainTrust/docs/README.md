# TF::GoogleBeta::GoogleActiveDirectoryDomainTrust

CloudFormation equivalent of google_active_directory_domain_trust

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleActiveDirectoryDomainTrust",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#selectiveauthentication" title="SelectiveAuthentication">SelectiveAuthentication</a>" : <i>Boolean</i>,
        "<a href="#targetdnsipaddresses" title="TargetDnsIpAddresses">TargetDnsIpAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetdomainname" title="TargetDomainName">TargetDomainName</a>" : <i>String</i>,
        "<a href="#trustdirection" title="TrustDirection">TrustDirection</a>" : <i>String</i>,
        "<a href="#trusthandshakesecret" title="TrustHandshakeSecret">TrustHandshakeSecret</a>" : <i>String</i>,
        "<a href="#trusttype" title="TrustType">TrustType</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleActiveDirectoryDomainTrust
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#selectiveauthentication" title="SelectiveAuthentication">SelectiveAuthentication</a>: <i>Boolean</i>
    <a href="#targetdnsipaddresses" title="TargetDnsIpAddresses">TargetDnsIpAddresses</a>: <i>
      - String</i>
    <a href="#targetdomainname" title="TargetDomainName">TargetDomainName</a>: <i>String</i>
    <a href="#trustdirection" title="TrustDirection">TrustDirection</a>: <i>String</i>
    <a href="#trusthandshakesecret" title="TrustHandshakeSecret">TrustHandshakeSecret</a>: <i>String</i>
    <a href="#trusttype" title="TrustType">TrustType</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Domain

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectiveAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDnsIpAddresses

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustDirection

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustHandshakeSecret

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrustType

_Required_: Yes

_Type_: String

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

