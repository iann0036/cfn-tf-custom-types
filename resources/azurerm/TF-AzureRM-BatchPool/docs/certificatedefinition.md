# TF::AzureRM::BatchPool CertificateDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#storelocation" title="StoreLocation">StoreLocation</a>" : <i>String</i>,
    "<a href="#storename" title="StoreName">StoreName</a>" : <i>String</i>,
    "<a href="#visibility" title="Visibility">Visibility</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#storelocation" title="StoreLocation">StoreLocation</a>: <i>String</i>
<a href="#storename" title="StoreName">StoreName</a>: <i>String</i>
<a href="#visibility" title="Visibility">Visibility</a>: <i>
      - String</i>
</pre>

## Properties

#### Id

The ID of the Batch Certificate to install on the Batch Pool, which must be inside the same Batch Account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreLocation

The location of the certificate store on the compute node into which to install the certificate. Possible values are `CurrentUser` or `LocalMachine`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreName

The name of the certificate store on the compute node into which to install the certificate. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). Common store names include: `My`, `Root`, `CA`, `Trust`, `Disallowed`, `TrustedPeople`, `TrustedPublisher`, `AuthRoot`, `AddressBook`, but any custom store name can also be used. The default value is `My`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Which user accounts on the compute node should have access to the private data of the certificate.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

