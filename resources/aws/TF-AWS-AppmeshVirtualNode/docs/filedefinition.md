# TF::AWS::AppmeshVirtualNode FileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificatechain" title="CertificateChain">CertificateChain</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#certificatechain" title="CertificateChain">CertificateChain</a>: <i>String</i>
</pre>

## Properties

#### CertificateChain

The certificate trust chain for a certificate stored on the file system of the mesh endpoint that the proxy is running on. Must be between 1 and 255 characters in length.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

