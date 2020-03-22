# Terraform::Vault::AwsAuthBackendLogin

Logs into a Vault server using an AWS auth backend. Login can be
accomplished using a signed identity request from IAM or using ec2
instance metadata. For more information, see the [Vault
documentation](https://www.vaultproject.io/docs/auth/aws.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AwsAuthBackendLogin",
    "Properties" : {
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#iamhttprequestmethod" title="IamHttpRequestMethod">IamHttpRequestMethod</a>" : <i>String</i>,
        "<a href="#iamrequestbody" title="IamRequestBody">IamRequestBody</a>" : <i>String</i>,
        "<a href="#iamrequestheaders" title="IamRequestHeaders">IamRequestHeaders</a>" : <i>String</i>,
        "<a href="#iamrequesturl" title="IamRequestUrl">IamRequestUrl</a>" : <i>String</i>,
        "<a href="#identity" title="Identity">Identity</a>" : <i>String</i>,
        "<a href="#nonce" title="Nonce">Nonce</a>" : <i>String</i>,
        "<a href="#pkcs7" title="Pkcs7">Pkcs7</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#signature" title="Signature">Signature</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AwsAuthBackendLogin
Properties:
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#iamhttprequestmethod" title="IamHttpRequestMethod">IamHttpRequestMethod</a>: <i>String</i>
    <a href="#iamrequestbody" title="IamRequestBody">IamRequestBody</a>: <i>String</i>
    <a href="#iamrequestheaders" title="IamRequestHeaders">IamRequestHeaders</a>: <i>String</i>
    <a href="#iamrequesturl" title="IamRequestUrl">IamRequestUrl</a>: <i>String</i>
    <a href="#identity" title="Identity">Identity</a>: <i>String</i>
    <a href="#nonce" title="Nonce">Nonce</a>: <i>String</i>
    <a href="#pkcs7" title="Pkcs7">Pkcs7</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#signature" title="Signature">Signature</a>: <i>String</i>
</pre>

## Properties

#### Backend

The unique name of the AWS auth backend. Defaults to
'aws'.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamHttpRequestMethod

The HTTP method used in the signed IAM
request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestBody

The base64-encoded body of the signed
request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestHeaders

The base64-encoded, JSON serialized
representation of the GetCallerIdentity HTTP request headers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamRequestUrl

The base64-encoded HTTP URL used in the signed
request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Identity

The base64-encoded EC2 instance identity document to
authenticate with. Can be retrieved from the EC2 metadata server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nonce

The unique nonce to be used for login requests. Can be
set to a user-specified value, or will contain the server-generated value
once a token is issued. EC2 instances can only acquire a single token until
the whitelist is tidied again unless they keep track of this nonce.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pkcs7

The PKCS#7 signature of the identity document to
authenticate with, with all newline characters removed. Can be retrieved from
the EC2 metadata server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The name of the AWS auth backend role to create tokens
against.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signature

The base64-encoded SHA256 RSA signature of the
instance identity document to authenticate with, with all newline characters
removed. Can be retrieved from the EC2 metadata server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Accessor

Returns the <code>Accessor</code> value.

#### AuthType

Returns the <code>AuthType</code> value.

#### ClientToken

Returns the <code>ClientToken</code> value.

#### Id

Returns the <code>Id</code> value.

#### LeaseDuration

Returns the <code>LeaseDuration</code> value.

#### LeaseStartTime

Returns the <code>LeaseStartTime</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### Policies

Returns the <code>Policies</code> value.

#### Renewable

Returns the <code>Renewable</code> value.

