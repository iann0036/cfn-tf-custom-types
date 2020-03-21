# Terraform::Google::ContainerCluster MasterAuth

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>" : <i>[ <a href="masterauth-clientcertificateconfig.md">ClientCertificateConfig</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>: <i>
      - <a href="masterauth-clientcertificateconfig.md">ClientCertificateConfig</a></i>
</pre>

## Properties

#### Password

The password to use for HTTP basic authentication when accessing
the Kubernetes master endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username to use for HTTP basic authentication when accessing
the Kubernetes master endpoint. If not present basic auth will be disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateConfig

_Required_: No

_Type_: List of <a href="masterauth-clientcertificateconfig.md">ClientCertificateConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

