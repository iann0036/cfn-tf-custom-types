# TF::Google::ContainerCluster DatabaseEncryptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
<a href="#state" title="State">State</a>: <i>String</i>
</pre>

## Properties

#### KeyName

the key to use to encrypt/decrypt secrets.  See the [DatabaseEncryption definition](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#Cluster.DatabaseEncryption) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

`ENCRYPTED` or `DECRYPTED`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

