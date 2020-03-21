# Terraform::Google::ComputeInstance NetworkInterface AccessConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#natip" title="NatIp">NatIp</a>" : <i>String</i>,
    "<a href="#networktier" title="NetworkTier">NetworkTier</a>" : <i>String</i>,
    "<a href="#publicptrdomainname" title="PublicPtrDomainName">PublicPtrDomainName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#natip" title="NatIp">NatIp</a>: <i>String</i>
<a href="#networktier" title="NetworkTier">NetworkTier</a>: <i>String</i>
<a href="#publicptrdomainname" title="PublicPtrDomainName">PublicPtrDomainName</a>: <i>String</i>
</pre>

## Properties

#### NatIp

The IP address that will be 1:1 mapped to the instance's
network ip. If not given, one will be generated.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkTier

The [networking tier][network-tier] used for configuring this instance.
This field can take the following values: PREMIUM or STANDARD. If this field is
not specified, it is assumed to be PREMIUM.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicPtrDomainName

The DNS domain name for the public PTR record.
To set this field on an instance, you must be verified as the owner of the domain.
See [the docs](https://cloud.google.com/compute/docs/instances/create-ptr-record) for how
to become verified as a domain owner.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

