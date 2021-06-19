# TF::AzureRM::KubernetesCluster WindowsProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
</pre>

## Properties

#### AdminPassword

The Admin Password for Windows VMs. Length must be between 14 and 123 characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

The Admin Username for Windows VMs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

