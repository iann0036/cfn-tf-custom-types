# TF::AWS::Apigatewayv2DomainName MutualTlsAuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#truststoreuri" title="TruststoreUri">TruststoreUri</a>" : <i>String</i>,
    "<a href="#truststoreversion" title="TruststoreVersion">TruststoreVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#truststoreuri" title="TruststoreUri">TruststoreUri</a>: <i>String</i>
<a href="#truststoreversion" title="TruststoreVersion">TruststoreVersion</a>: <i>String</i>
</pre>

## Properties

#### TruststoreUri

An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, `s3://bucket-name/key-name`.
The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TruststoreVersion

The version of the S3 object that contains the truststore. To specify a version, you must have versioning enabled for the S3 bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

