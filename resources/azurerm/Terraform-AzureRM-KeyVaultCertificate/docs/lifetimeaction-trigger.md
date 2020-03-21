# Terraform::AzureRM::KeyVaultCertificate LifetimeAction Trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#daysbeforeexpiry" title="DaysBeforeExpiry">DaysBeforeExpiry</a>" : <i>Double</i>,
    "<a href="#lifetimepercentage" title="LifetimePercentage">LifetimePercentage</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#daysbeforeexpiry" title="DaysBeforeExpiry">DaysBeforeExpiry</a>: <i>Double</i>
<a href="#lifetimepercentage" title="LifetimePercentage">LifetimePercentage</a>: <i>Double</i>
</pre>

## Properties

#### DaysBeforeExpiry

The number of days before the Certificate expires that the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with `lifetime_percentage`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimePercentage

The percentage at which during the Certificates Lifetime the action associated with this Trigger should run. Changing this forces a new resource to be created. Conflicts with `days_before_expiry`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

