# TF::GoogleBeta::GoogleContainerCluster MasterAuthDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>,
    "<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>" : <i>[ <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
<a href="#clientcertificateconfig" title="ClientCertificateConfig">ClientCertificateConfig</a>: <i>
      - <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a></i>
</pre>

## Properties

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificateConfig

_Required_: No

_Type_: List of <a href="clientcertificateconfigdefinition.md">ClientCertificateConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

