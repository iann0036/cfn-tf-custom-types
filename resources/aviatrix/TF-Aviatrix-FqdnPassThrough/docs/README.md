# TF::Aviatrix::FqdnPassThrough

The **aviatrix_fqdn_pass_through** resource manages FQDN filter pass-through for Aviatrix gateways.

~> **NOTE:** The **aviatrix_fqdn_pass_through** resource must be created after the **aviatrix_fqdn** resource to be created successfully. To ensure that Terraform orders the creation of these resources correctly please use a `depends_on` meta-argument so that the **aviatrix_fqdn** resource is created before the **aviatrix_fqdn_pass_through** resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::FqdnPassThrough",
    "Properties" : {
        "<a href="#gwname" title="GwName">GwName</a>" : <i>String</i>,
        "<a href="#passthroughcidrs" title="PassThroughCidrs">PassThroughCidrs</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::FqdnPassThrough
Properties:
    <a href="#gwname" title="GwName">GwName</a>: <i>String</i>
    <a href="#passthroughcidrs" title="PassThroughCidrs">PassThroughCidrs</a>: <i>
      - String</i>
</pre>

## Properties

#### GwName

Gateway name to apply pass-through rules to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassThroughCidrs

List of origin CIDR's to allow to pass-through FQDN filtering rules. Minimum list length: 1.

_Required_: Yes

_Type_: List of String

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

